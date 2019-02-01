class ArianaClient {
    constructor(axios) {
        this.http = axios
    }

    async questionnaireList() {
        return await this.http.get('questionnaire/')
    }

    async questionnaireCreate(questionnaireId) {
        return await this.http.post('questionnaire/', {
            id: questionnaireId
        })
    }

    async questionnaireSessionRetrieve(questionnaireSessionId) {
        return await this.http.get('questionnaire/session/', {
            params: {
                id: questionnaireSessionId
            }
        })
    }

    async questionnaireSessionSubmitAnswer(questionnaireSessionId, answerId) {
        return await this.http.post('questionnaire/session/', {
            'questionnaire_id': questionnaireSessionId,
            'answer_id': answerId
        })
    }
}

// noinspection JSUnusedGlobalSymbols
export default ArianaClient
