<template>
  <teleport to="body">
    <ModelessDialog
      :title="'アーティスト詳細'"
      class="content-width"
      :positionTop="positionTop+'px'"
      :positionLeft="positionLeft+'px'"
      @close-dialog="$emit('close')"
    >
      <div>
        <h1>{{ artistInfo.artist }}</h1>
        <div class="row">
          <div class="col-xs-12 col-md-5 pt-3">
            <img :src="'/assets/'+artistInfo.img" class="border rounded img-width">
          </div>
          <div class="col-md-1"></div>
          <div class="col-xs-12 col-md-6">
            <h3>favorite songs</h3>
            <div
              class="mb-1"
              v-for="(song, index) in artistInfo.song"
              :key="index"
            ><i class="bi bi-music-note"></i>{{ song }}
            </div>
          </div>
        </div>
        <div v-html="artistInfo.comment" class="my-3"></div>
      </div>
    </ModelessDialog>
  </teleport>
</template>

<script>
import { defineComponent, computed } from "vue"
import ModelessDialog from "@/components/ModelessDialog"
import allArtist from "@/assets/json/artist.json"

export default defineComponent({
  components: {
    ModelessDialog
  },
  props: {
      positionX: String,
      positionY: String,
      artist: String,
      stage: String
  },
  emits: [
    "close"
  ],
  setup(props) {
    const positionTop = computed(() => props.positionY - 150)
    const positionLeft = computed(() => props.positionX - 300)
    const artistInfo = computed(() => allArtist[props.stage].filter(data => data.artist == props.artist)[0])

    return {
      positionTop,
      positionLeft,
      artistInfo
    }
  }
})
</script>

<style scoped>
.img-width {
  width: 200px;
}

</style>