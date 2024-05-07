<template>

    <div class="collapse bg-base-200 m-3" v-for="item in myArray" :key="item">
    <input type="radio" name="my-accordion-1" checked="checked" /> 
        <div class="collapse-title text-xl font-medium">
        {{ item }}
        </div>
        <div class="collapse-content"> 
            <p>域名状况</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'subdomainList',
    props: {
    myArray: {
      type: Array,
      required: true
    }
  }
}
</script>