<template>
    <section id="pets-resume">
        <nav class="level">
          <div class="level-item has-text-centered">
            <div>
              <p class="heading">{{ $t("found") }}</p>
              <p class="title">3,456</p>
            </div>
          </div>
          <div class="level-item has-text-centered">
            <div>
              <p class="heading">{{ $t("rescued") }}</p>
              <p class="title">123</p>
            </div>
          </div>
          <div class="level-item has-text-centered">
            <div>
              <p class="heading">{{ $t("adopted") }}</p>
              <p class="title">456K</p>
            </div>
          </div>
          <div class="level-item has-text-centered">
            <div>
              <p class="heading">{{ $t("likes") }}</p>
              <p class="title">789</p>
            </div>
          </div>
        </nav>
    </section>
</template>

<script>
export default {};
</script>

<style>
    #pets-resume {
        margin-top: 40px;
        margin-bottom: 40px;
    }
</style>

<i18n>
{
  "en": {
    "found": "Found",
    "rescued": "Rescued",
    "adopted": "Adopted",
    "likes": "Likes"
  },
  "es": {
    "found": "Encontradas",
    "rescued": "Rescatadas",
    "adopted": "Adoptadas",
    "likes": "Likes"
  }
}
</i18n>
