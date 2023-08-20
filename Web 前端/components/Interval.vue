<template>
  Interval fired:{{counter}}
</template>
<script setup>
import { useInterval } from '@vueuse/core'
const counter = useInterval(2000)
</script>
