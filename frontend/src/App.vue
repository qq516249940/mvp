<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="scss">

  // Import Bulma's core
  @import "~bulma/sass/utilities/_all";

  // Set your colors
  $primary: #fa6e6f;
  $primary-invert: findColorInvert($primary);
  $bulma: #00d1b2;
  $bulma-invert: findColorInvert($bulma);
  $buefy: #7957d5;
  $buefy-invert: findColorInvert($buefy);

  // Setup $colors to use as bulma classes (e.g. 'is-twitter')
  $colors: (
  "white": ($white, $black),
  "black": ($black, $white),
  "light": ($light, $light-invert),
  "dark": ($dark, $dark-invert),
  "primary": ($primary, $primary-invert),
  "info": ($info, $info-invert),
  "success": ($success, $success-invert),
  "warning": ($warning, $warning-invert),
  "danger": ($danger, $danger-invert),
  "bulma": ($bulma, $bulma-invert),
  "buefy": ($buefy, $buefy-invert)
  );

  // Links
  $link: $primary;
  $link-invert: $primary-invert;
  $link-focus-border: $primary;

  // Import Bulma and Buefy styles
  @import "~bulma";
  @import "~buefy/src/scss/buefy";

  // Custom CSS
  i {
    margin-right: 10px;
  }

  /* Animations */
  .animated {
    -webkit-animation-duration: 1.5s;
    animation-duration: 1.5s;
    -webkit-animation-fill-mode: both;
    animation-fill-mode: both;
  }

  .fast {
    -webkit-animation-duration: 0.4s;
    animation-duration: 0.4s;
    -webkit-animation-fill-mode: both;
    animation-fill-mode: both;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  .fadeIn {
    animation-name: fadeIn;
  }

</style>
