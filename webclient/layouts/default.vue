<template>
    <div class="wrapper">
        <header>
            <b-navbar toggleable type="light" variant="light">
                <b-navbar-toggle target="nav_text_collapse"></b-navbar-toggle>

                <b-navbar-brand href="/">
                    <img class="logo d-inline-block align-top" src="../assets/images/logo.jpg" alt=""/>
                </b-navbar-brand>

                <b-collapse is-nav id="nav_text_collapse">
                    <b-navbar-nav>
                        <b-nav-item :to="{name: 'index'}">Home</b-nav-item>
                        <b-nav-item :to="{name: 'questionnaires'}">Questionnaires</b-nav-item>
                    </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </header>
        <main class="main-content">
            <nuxt/>
        </main>
    </div>
</template>
<script>

export default {}
</script>
