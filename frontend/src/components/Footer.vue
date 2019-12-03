<template>
    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          <strong>Rescaty</strong> {{ $t("by")}} <a href="https://github.com/rescaty">
          Rescaty Devs</a>.<br>{{ $t("source")}}
          <a href="http://opensource.org/licenses/mit-license.php">MIT</a>.<br>
          {{ $t("website")}}
          <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY NC SA 4.0</a>.
          <br>{{ $t("mvp")}}
          <a href="https://en.wikipedia.org/wiki/Minimum_viable_product">MVP</a>,
          {{ $t("mpvNote")}}
        </p>
      </div>
    </footer>
</template>

<script>
export default {};
</script>

<i18n>
{
  "en": {
    "by": "by",
    "source": "The source code is licensed",
    "website": "The website content is licensed",
    "mvp": "This is an",
    "mpvNote": "a lot of functionality is not yet implemented."
  },
  "es": {
    "by": "por",
    "source": "El codigo fuente esta licencidado",
    "website": "El contenido del sitio web esta licenciado",
    "mvp": "Este es un",
    "mpvNote": "Mucha de la funcionalidad no esta todavia implementada."
  }

}
</i18n>
