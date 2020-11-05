<template>
<div class="hoge1">
  hoge {{ val }}
</div>
</template>


<script>
export default {
  components: {},
  data () {
    return {
      val: 1,
    }
  },
}
</script>

<style>
.hoge1 {
  width: 100%; height: 100%;
  background-color: gray;
}
</style>