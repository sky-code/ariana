<template>
    <div>
        <div>
            <b-card-group deck>
                <b-card v-for="item in questionnaireList" :key="item.id" :title="item.name">
                    <p class="card-text">{{item}}</p>
                    <b-button @click="newQuestionnaire(item.id)"
                              v-wait:disabled="'newQuestionnaire'"
                              variant="primary">Start
                    </b-button>
                </b-card>
            </b-card-group>
        </div>
    </div>
</template>

<script>
import {waitFor} from 'vue-wait'

export default {
    async asyncData({app, params}) {
        let {data} = await app.$arianaClient.questionnaireList()

        return {questionnaireList: data}
    },
    methods: {
        newQuestionnaire: waitFor('newQuestionnaire', async function (questionnaireId) {
            let {data} = await this.$arianaClient.questionnaireCreate(questionnaireId)
            this.$router.push({
                name: 'questionnaire-id',
                params: {id: data.id}
            })
        })
    }
}
</script>
