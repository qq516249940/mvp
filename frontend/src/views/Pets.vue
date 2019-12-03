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
      <br>
      <br>
      <div class="container">
        <h1 class="title">
          {{ $t("lastReported") }}
        </h1>
        <div class="tile is-ancestor">
            <Pet v-for="pet in lastPets" :pet="pet" :key="pet.id"/>
        </div>
        <br>
        <h1 class="title">
          {{ $t("search") }}
        </h1>
        <section>
          <b-tabs v-model="statusIndex"
          position="is-centered"
          type="is-boxed"
          size="is-normal"
          expanded>
              <b-tab-item :label="$t('status.missing')"
              icon="crosshairs-question"></b-tab-item>
              <b-tab-item :label="$t('status.found')"
              icon="crosshairs-gps"></b-tab-item>
              <b-tab-item :label="$t('status.adoption')"
              icon="star-circle-outline"></b-tab-item>
              <b-tab-item :label="$t('status.adopted')"
              icon="shield-star-outline"></b-tab-item>
              <b-tab-item :label="$t('status.rescued')"
              icon="ambulance"></b-tab-item>
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
      </section>
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
      status: [
        'missing',
        'found',
        'adoption',
        'adopted',
        'rescued',
      ],
    };
  },
  watch: {
    statusIndex() {
      this.pagCurrent = 1;
      this.kind = 'Any';
      this.getPets();
    },
    kind() {
      this.pagCurrent = 1;
      this.getPets();
    },
    pagCurrent() {
      this.getPets();
    },
  },
  computed: {
    getStatus() {
      return this.status[this.statusIndex];
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
    getPets() {
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
    this.getPets();
  },
};
</script>

<i18n>
{
  "en": {
    "title": "Reported Pets",
    "subtitle": "Search for your pet",
    "lastReported": "Last reported...",
    "search": "Search...",
    "status": {
      "missing": "Missing",
      "found": "Found",
      "adoption": "Adoption",
      "adopted": "Adopted",
      "rescued": "Rescued"
    }
  },
  "es": {
    "title": "Mascotas Reportadas",
    "subtitle": "Busca tu mascota",
    "lastReported": "Ultimos reportes...",
    "search": "Busqueda...",
    "status": {
      "missing": "Perdido",
      "found": "Encontrado",
      "adoption": "En adopcion",
      "adopted": "Adoptado",
      "rescued": "Rescatado"
    }
  }
}
</i18n>
