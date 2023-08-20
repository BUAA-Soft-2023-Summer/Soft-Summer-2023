<template>
{{ now }}
</template>

<script setup>
import { useNow , useDateFormat} from '@vueuse/core'
const now = useDateFormat(useNow(), 'YYYY-MM-DD HH:mm:ss')
</script>
