<template>
    <section>
    <NavBar/>
      <section class="hero is-primary">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              Reported Pets
            </h1>
            <h2 class="subtitle">
              Search for your pet
            </h2>
          </div>
        </div>
      </section>
      <br>
      <br>
      <div class="container">
        <h1 class="title">
          Last reported...
        </h1>
        <div class="tile is-ancestor">
            <Pet v-for="pet in lastPets" :pet="pet" :key="pet.id"/>
        </div>
        <br>
        <h1 class="title">
          Filtering...
        </h1>
        <section>
          <b-tabs v-model="statusIndex"
          position="is-centered"
          type="is-boxed"
          size="is-medium"
          expanded>
              <b-tab-item label="Missing"
              icon="google-photos"></b-tab-item>
              <b-tab-item label="Found"
              icon="library-music"></b-tab-item>
              <b-tab-item label="Adoption"
              icon="video"></b-tab-item>
              <b-tab-item label="Adopted"
              icon="video"></b-tab-item>
              <b-tab-item label="Rescued"
              icon="video"></b-tab-item>
          </b-tabs>
          <div class="block">
            <b-radio v-model="kind"
                name="kind"
                native-value="Any">
                Any
            </b-radio>
            <b-radio v-model="kind"
                name="kind"
                native-value="Dog">
                Dog
            </b-radio>
            <b-radio v-model="kind"
                name="kind"
                native-value="Cat">
                Cat
            </b-radio>
          </div>
          <div class="tile is-ancestor">
            <Pet v-for="pet in filteredPets" :pet="pet" :key="pet.id"/>
        </div>
        <b-pagination
            :total="totalPets"
            :current.sync="pagCurrent"
            :per-page="pagination"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page">
        </b-pagination>
        </section>
      </div>
      <br>
      <br>
      <Footer/>
    </section>
</template>

<script>
import Pet from '@/components/Pet.vue';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';

import { API } from '@/conf/conf';


export default {
  components: {
    NavBar,
    Pet,
    Footer,
  },
  data() {
    return {
      loading: false,
      pagination: 5,
      pagCurrent: 1,
      totalPets: 5,
      kind: 'Any',
      statusIndex: 0,
      lastPets: [],
      lastPetsLimit: 3,
      filteredPets: [],
    };
  },
  watch: {
    statusIndex() {
      this.pagCurrent = 1;
      this.kind = 'Any';
      this.getNextPets();
    },
    kind() {
      this.pagCurrent = 1;
      this.getNextPets();
    },
    pagCurrent() {
      this.getNextPets();
    },
  },
  computed: {
    getStatus() {
      const tabs = [
        'Missing',
        'Found',
        'Adoption',
        'Adopted',
        'Rescued',
      ];
      return tabs[this.statusIndex];
    },
    getKind() {
      if (this.kind === 'Any') {
        return '';
      }
      return this.kind;
    },
  },
  methods: {
    getLastPets() {
      this.$http.get(`${API.protocol}${API.host}${API.api}/pets/?limit=${this.lastPetsLimit}`)
        .then((resp) => {
          this.lastPets = resp.data.pets;
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    getNextPets() {
      let skip = this.pagination * (this.pagCurrent - 1);
      if (skip < 0) {
        skip = 0;
      }
      console.log(skip);
      this.$http.get(`${API.protocol}${API.host}${API.api}/pets/`
        + `?status=${this.getStatus}&kind=${this.getKind}`
        + `&limit=${this.pagination}&skip=${skip}`)
        .then((resp) => {
          this.filteredPets = resp.data.pets;
          this.totalPets = resp.data.count;
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    getPetsStats() {},
  },
  created() {
    this.getPetsStats();
    this.getLastPets();
    this.getNextPets();
  },
};
</script>
