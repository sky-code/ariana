<template>
    <div>
        <b-card :title="qs.questionnaireName">
            <template v-if="qs.finished">
                <p class="card-text">{{qs.questionTitle}}</p>
                <p class="card-text">Questionnaire finished</p>
            </template>
            <template v-else>
                <p class="card-text">{{qs.questionTitle}}</p>
                <div v-for="answer in qs.questionAnswers" :key="answer.id">
                    <b-button @click="submitAnswer(answer.id)"
                              v-wait:disabled="'submitAnswer'"
                              variant="primary">
                        {{answer.title}}
                    </b-button>
                </div>
            </template>
        </b-card>
    </div>
</template>

<script>
import {waitFor} from 'vue-wait'

export default {
    async asyncData({app, params}) {
        const qsId = params.id
        const {data} = await app.$arianaClient.questionnaireSessionRetrieve(qsId)

        return {qsId: qsId, qs: data}
    },
    methods: {
        submitAnswer: waitFor('submitAnswer', async function (answerId) {
            try {
                const response = await this.$arianaClient.questionnaireSessionSubmitAnswer(this.qsId, answerId)
                this.qs = response.data
            } catch (e) {
                alert('Some error occurred, please try again')
                const {data} = await app.$arianaClient.questionnaireSessionRetrieve(this.qsId)
                this.qs = data
            }
        })
    }
}
</script>
