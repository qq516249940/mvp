<template>
    <section v-if="pet.status">
        <div class="tile is-parent">
            <article class="tile is-child notification is-primary">
                <p class="title">{{ pet.status }} - {{ pet.kind }}</p>
                <figure v-if="imageData.status === 'success'" class="image is-4by3">
                    <img :src="imageData.message">
                </figure>
                <p v-if="pet.name" class="subtitle">Name: {{ pet.name }}</p>
                <p class="subtitle">{{ pet.story}}</p>
                <p class="subtitle">Location: {{ pet.location }}</p>
                <p class="subtitle">id: {{ pet.id_ }}</p>
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
