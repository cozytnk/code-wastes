<template>
<div class="hoge3">
  hoge {{ val }}
</div>
</template>


<script>
export default {
  components: {},
  data () {
    return {
      val: 3,
    }
  },
}
</script>

<style>
.hoge3 {
  width: 100%; height: 100%;
  background-color: gray;
}
</style>