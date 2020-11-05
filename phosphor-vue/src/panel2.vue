<template>
<div class="hoge2">
  hoge {{ val }}
</div>
</template>


<script>
export default {
  components: {},
  data () {
    return {
      val: 2,
    }
  },
}
</script>

<style>
.hoge2 {
  width: 100%; height: 100%;
  background-color: pink;
}
</style>