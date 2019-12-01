<template>
    <b-navbar shadow fixed-top>
        <template slot="brand">
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <img
                    src="../assets/logo_transparent_simple.png"
                    alt="Lightweight UI components for Vue.js based on Bulma"
                >
            <b-icon
                icon="dog"
                size="is-large">
            </b-icon>
            </b-navbar-item>
        </template>
        <template slot="start">
            <b-navbar-item href="#">
                <b-icon
                    icon="map-search"
                    size="is-small">
                </b-icon>
                Pets
            </b-navbar-item>
            <b-navbar-item href="#">
                <b-icon
                    icon="alarm-light-outline"
                    size="is-small">
                </b-icon>
                Bad Actor
            </b-navbar-item>
            <b-navbar-item tag="router-link" :to="{ path: '/about' }">
                <b-icon
                    icon="information-outline"
                    size="is-small">
                </b-icon>
                About
            </b-navbar-item>
        </template>

        <template slot="end">
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a class="button is-primary">
                        <b-icon icon="tooltip-plus-outline"></b-icon>
                        <strong>Report Pet</strong>
                    </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
export default {};
</script>
