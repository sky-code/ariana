import ArianaClient from "~/app/ariana-client"

export default function (ctx, inject) {
    // Check axios module is correctly registered
    if (!ctx.$axios) {
        console.error('[ariana-client-plugin]', 'Please make sure @nuxtjs/axios is added after this plugin!')
    }
    // Inject $ctx
    const arianaClient = new ArianaClient(ctx.$axios)
    inject('arianaClient', arianaClient)
}
