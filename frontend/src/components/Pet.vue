<template>
    <section v-if="pet.status">
        <div class="tile is-parent">
            <article class="tile is-child notification is-primary">
                <p class="title">
                  {{ $t("pet.status." + pet.status) }} - {{ $t("pet.kind." + pet.kind) }}
                </p>
                <p class="subtitle">ID: {{ pet.id_ }}</p>
                <figure v-if="imageData.status === 'success'" class="image is-4by3">
                    <img :src="imageData.message">
                </figure>
                <p v-if="pet.name" class="subtitle">
                  {{ $t("pet.name") }}: {{ pet.name }}
                </p>
                <p class="subtitle">{{ pet.story}}</p>
                <p class="subtitle">
                  {{ $t("pet.location")}}: {{ pet.location }}</p>
                <p class="subtitle">
                  {{ $t("pet.last_modified") }}: {{ $d(new Date(pet.last_modified + 'Z'), 'long') }}
                </p>
            </article>
        </div>
    </section>
</template>

<script>
export default {
  props: {
    pet: {
      required: true,
      type: Object,
    },
  },
  data() {
    return {
      imageData: {},
    };
  },
  methods: {
    getPic() {
      this.$http.get('https://dog.ceo/api/breeds/image/random')
        .then((resp) => {
          this.imageData = resp.data;
        });
    },
  },
  created() {
    this.getPic();
  },
};
</script>

<i18n>
{
  "en": {
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
    }
  },
  "es": {
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
    }
  }
}
</i18n>
