<template lang="html">
  <div class="page-loader" v-if="loading">
      <img src="~/assets/images/loading.svg" alt="" />
  </div>
</template>

<script>
export default {
  data: () => ({
    loading: false
  }),
  methods: {
    start () {
      this.loading = true
    },
    finish () {
      this.loading = false
    }
  }
}
</script>
