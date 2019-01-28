import path from 'path'

import dotenv from 'dotenv'
// load .env file into process.env
dotenv.config()

// noinspection JSUnresolvedVariable
const rootDir = path.resolve(__dirname);
export default {
    /*
    ** Headers of the page
    */
    head: {
        title: 'Ariana',
        meta: [
            {charset: 'utf-8'},
            {name: 'viewport', content: 'width=device-width, initial-scale=1'},
            {hid: 'description', name: 'description', content: '{{ description }}'}
        ],
        link: [
            {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'}
        ]
    },
    /*
    ** Customize the progress bar color
    */
    loading: 'components/loading.vue',
    srcDir: 'webclient/',
    /*
    ** Build configuration
    */
    build: {
        transpile: []
    },
    css: [
        'bootstrap/dist/css/bootstrap.min.css',
        '~/assets/styles/index.scss',
    ],
    plugins: [],
    /*
    ** Additional modules
     */
    modules: [
        ['@nuxtjs/dotenv', {
            path: rootDir,
            only: ['ARIANA_WEB_API_URL', 'ARIANA_WEB_API_SSR_URL']
        }],
        ['bootstrap-vue/nuxt', {css: false}],
        ['vue-wait/nuxt', {useVuex: false}],
    ]
}
