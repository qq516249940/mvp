<template>
    <section>
      <NavBar/>
      <section class="animated fadeIn">
        <section class="hero is-primary">
          <div class="hero-body">
            <div class="container">
              <h1 class="title">
                {{ $t("title") }}
              </h1>
              <h2 class="subtitle">
                {{ $t("subtitle") }}
              </h2>
            </div>
          </div>
        </section>
        <div class="container" id="add-pet-form">
            <div v-if="newPet" class="columns is-mobile animated fadeIn">
              <div class="column is-half is-offset-one-quarter">
                <Pet :pet="newPet" />
              </div>
              <br>
              <br>
            </div>
            <section class="animated fadeIn">
              <div class="columns is-mobile">
                <div class="column is-three-fifths is-offset-one-fifth">
                  <form @submit="addPet">
                    <b-field :label="$t('kind')">
                        <b-select v-model="pet.kind" :placeholder="$t('select')" required>
                            <option v-for="(_, kind) in kinds" :value="kind" v-bind:key="kind">
                              {{ $t('pet.kind.' + kind) }}
                            </option>
                        </b-select>
                    </b-field>

                    <b-field :label="$t('status')">
                        <b-select v-model="pet.status" :placeholder="$t('select')" required>
                            <option v-for="(_, sts) in status" :value="sts" v-bind:key="sts">
                             {{ $t('pet.status.' + sts) }}
                            </option>
                        </b-select>
                    </b-field>

                    <b-field :label="$t('location')">
                        <b-input
                        v-model="pet.location"
                        :placeholder="$t('locationPlaceHolder')"
                        required></b-input>
                    </b-field>

                    <b-field :label="$t('name')">
                        <b-input v-model="pet.name" :placeholder="$t('namePlaceHolder')"></b-input>
                    </b-field>

                    <b-field :label="$t('story')">
                        <b-input v-model="pet.story"
                        :placeholder="$t('storyPlaceHolder')"
                        type="textarea"
                        required></b-input>
                    </b-field>

                    <b-button
                    type="is-primary"
                    native-type="submit"
                    outlined>{{ $t("submit") }}</b-button>
                  </form>
                </div>
              </div>
            </section>
        </div>
        <br>
        <br>
        <Footer/>
      </section>
    </section>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import Pet from '@/components/Pet.vue';

import { API } from '@/conf/conf';


export default {
  data() {
    return {
      loading: false,
      newPet: {},
      pet: {
        kind: null,
        status: null,
        location: null,
        name: null,
        story: null,
      },
      kinds: {
        dog: 'Dog',
        cat: 'Cat',
      },
      status: {
        missing: 'Missing',
        found: 'Found',
        adoption: 'Adoption',
        adopted: 'Adopted',
        rescued: 'Rescued',
      },
    };
  },
  methods: {
    addPet(e) {
      this.loading = true;
      e.preventDefault();

      this.$http.post(`${API.protocol}${API.host}${API.api}/pets/`, this.pet)
        .then((resp) => {
          console.log(resp.data);
          this.pet = {
            kind: '',
            status: '',
            location: '',
            name: '',
            story: '',
          };
          this.newPet = resp.data;
          this.$buefy.dialog.alert(this.$t('confirmation'));
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
  components: {
    NavBar,
    Footer,
    Pet,
  },
};
</script>

<style>
  #add-pet-form {
    margin-top: 40px;
    margin-bottom: 40px;
  }
</style>

<i18n>
{
  "en": {
    "title": "Report a Pet",
    "subtitle": "Add a pet",
    "select": "Select one",
    "kind": "Kind",
    "status": "Status",
    "location": "Location",
    "locationPlaceHolder": "Address",
    "name": "Name",
    "namePlaceHolder": "Optional",
    "story": "Story",
    "storyPlaceHolder": "Tell us what append to this pet, include all useful details...",
    "submit": "Report",
    "pet": {
      "kind": {
        "dog": "Dog",
        "cat": "Cat"
      },
      "status": {
        "missing": "Missing",
        "found": "Found",
        "adoption": "Adoption",
        "adopted": "Adopted",
        "rescued": "Rescued"
      },
      "story": "Story",
      "name": "Name",
      "location": "Location",
      "states": {
        "injured": "Injured",
        "underfed": "Underfed",
        "critical": "Critical",
        "bad": "Bad",
        "good": "Good",
        "healthy": "Healthy"
      },
      "picture": "Picture",
      "in_temp_house": "In temporal house",
      "created_at": "Created",
      "last_modified": "Updated"
    },
    "confirmation": "Thank you, this pet has been added."
  },
  "es": {
    "title": "Reportar una Mascota",
    "subtitle": "Agregar mascota",
    "select": "Selecionar",
    "kind": "Tipo",
    "status": "Estado",
    "location": "Locacion",
    "locationPlaceHolder": "Direccion o referencias",
    "name": "Nombre",
    "namePlaceHolder": "Opcional",
    "story": "Historia",
    "storyPlaceHolder": "Cuentanos que paso con esta mascota, incluye todos los detalles utiles.",
    "submit": "Report",
    "pet": {
      "kind": {
        "dog": "Perro",
        "cat": "Gato"
      },
      "status": {
        "missing": "Perdido",
        "found": "Encontrado",
        "adoption": "En adopcion",
        "adopted": "Adoptado",
        "rescued": "Rescatado"
      },
      "story": "History",
      "name": "Nombre",
      "location": "Locacion",
      "states": {
        "injured": "Lastimado",
        "underfed": "Desnutrido",
        "critical": "Critico",
        "bad": "Malo",
        "good": "Bueno",
        "healthy": "Sano"
      },
      "picture": "Foto",
      "in_temp_house": "En casa temporal",
      "created_at": "Agregado",
      "last_modified": "Actualizado"
    },
    "confirmation": "Gracias, esta mascota has been added."
  }
}
</i18n>
