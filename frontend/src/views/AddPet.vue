<template>
    <section>
        <NavBar/>
        <div class="container" id="add-pet-form">
            <section class="animated fadeIn">
                <form @submit="addPet">
                  <b-field label="Kind">
                      <b-select v-model="pet.kind" placeholder="Select a subject" required>
                          <option value="Dog">Dog</option>
                          <option value="Cat">Cat</option>
                      </b-select>
                  </b-field>

                  <b-field label="Status">
                      <b-select v-model="pet.status" placeholder="Select a subject" required>
                          <option value="Missing">Missing</option>
                          <option value="Found">Found</option>
                          <option value="For Adoption">For Adoption</option>
                          <option value="Adopted">Adopted</option>
                          <option value="Rescued">Rescued</option>
                      </b-select>
                  </b-field>

                  <b-field label="Location">
                      <b-input
                      v-model="pet.location"
                      placeholder="Address..."
                      required></b-input>
                  </b-field>

                  <b-field label="Name">
                      <b-input v-model="pet.name" placeholder="Optional"></b-input>
                  </b-field>

                  <b-field label="Story">
                      <b-input v-model="pet.story"
                      placeholder="Tell us what has append to this pet..."
                      type="textarea"
                      required></b-input>
                  </b-field>

                  <b-button
                  type="is-primary"
                  native-type="submit"
                  outlined>Report Pet</b-button>
                </form>
            </section>
        </div>
        <br>
        <br>
        <div  class="columns is-mobile">
          <div class="column is-half is-offset-one-quarter">
            <Pet v-if="newPet" :pet="newPet" />
          </div>
        </div>
        <Footer/>
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
        kind: '',
        status: '',
        location: '',
        name: '',
        story: '',
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
          this.$buefy.dialog.alert('This pet has been added');
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
