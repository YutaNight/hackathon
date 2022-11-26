<template>
  <teleport to="body">
    <ModelessDialog
      :title="'結線情報'"
      width="600px"
      positionTop="50%"
      positionLeft="40%"
      @close-dialog="$emit('close')"
    >
      <img :src="innerFilePath" alt="結線情報">
    </ModelessDialog>
  </teleport>
</template>

<script>
import { defineComponent, computed } from 'vue'
import { useStore } from 'vuex'
import ModelessDialog from "@/components/ModelessDialog"
export default defineComponent({
  name: "EquipLinksDialog",
  components: {
    ModelessDialog
  },
  emits: ["close"],
  setup(_, { emit }) {
    const store = useStore()
    const innerFilePath = computed(() => process.env.VUE_APP_IMAGE_URL + store.getters.getImageUrl)

    const close = () => emit("close")
    return {
      innerFilePath,
      close,
    }
  }
})
</script>