<template>
  <div class="bg-dark text-white">
    <h1 class="pt-5">ARTIST</h1>
    <h3>Please Click Artist Name for Detail. (Draggable)</h3>
    <div class="container">
      <div class="row">
        <div class="col-xs-12 col-md-4 px-0">
          <ArtistColumn :stage="'junior'" />
        </div>
        <div class="col-xs-12 col-md-4 px-0">
          <ArtistColumn :stage="'university'" />
        </div>
        <div class="col-xs-12 col-md-4 px-0">
          <ArtistColumn :stage="'worker'" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import ArtistColumn from "@/components/ArtistColumn"

export default defineComponent({
  components: {
    ArtistColumn,
  }
})
</script>

<style>

</style>