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
            <b-navbar-item tag="router-link" :to="{ name: 'pets' }">
                <b-icon
                    icon="magnify"
                    size="is-small">
                </b-icon>
                {{ $t("pets") }}
            </b-navbar-item>
            <b-navbar-item tag="router-link" :to="{ name: 'about' }">
                <b-icon
                    icon="star-outline"
                    size="is-small">
                </b-icon>
                {{ $t("about") }}
            </b-navbar-item>
        </template>

        <template slot="end">
            <b-navbar-item tag="router-link" :to="{ name: 'add' }">
                <a class="button is-primary">
                    <b-icon icon="tooltip-plus-outline"></b-icon>
                    <strong>{{ $t("reportPet") }}</strong>
                </a>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
export default {};
</script>

<i18n>
{
  "en": {
    "pets": "Pets",
    "about": "About",
    "reportPet": "Report Pet"
  },
  "es": {
    "pets": "Mascotas",
    "about": "Acerca",
    "reportPet": "Reportar"
  }
}
</i18n>
