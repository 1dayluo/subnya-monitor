<template>

    <!-- <div class="collapse bg-base-200 m-3" v-for="item in myArray" :key="item">
    <input type="radio" name="my-accordion-1" checked="checked" /> 
        <div class="collapse-title text-xl font-medium">
        {{ item.domain }} 
        
        <div v-if="item.status==='off'" class="badge">new</div>
        </div>
        <div class="collapse-content"> 
            <p>域名状况</p>
            {{ item.status }}
        </div>
    </div> -->

<div class="overflow-x-auto">
  <table class="table table-xs table-pin-rows table-pin-cols">
    <thead>
      <tr>
        <th></th> 
        <td>域名</td> 
        <td>同步状态</td> 
        <td>子域名数量</td> 
        <td>最后更新时间</td> 
        <th></th> 
      </tr>
    </thead> 
    <tbody>
        <div  v-for="item in myArray" :key="item">
            <tr>
              <div v-if="item.status==='off'" > 
                <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"> {{ myArray.indexOf(item) }} </td>
                <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ item.domain }} </td>
                <td class="whitespace-nowrap px-4 py-2 text-gray-700"> - </td>
                <td class="whitespace-nowrap px-4 py-2 text-gray-700"> - </td>
                <td class="whitespace-nowrap px-4 py-2 text-gray-700"> - </td>
              </div>
              <div v-else >
                <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"> {{ myArray.indexOf(item) }} </td>
                <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ item.domain }} </td>
                <td class="whitespace-nowrap px-4 py-2 text-gray-700"> on </td>
                <td class="whitespace-nowrap px-4 py-2 text-gray-700"> {{ item.subdomain_num }} </td>
                <td class="whitespace-nowrap px-4 py-2 text-gray-700"> {{ item.last }} </td>
              </div>
      		</tr>
      	</div>
    </tbody> 
    <tfoot>
      <tr>
        <th></th> 
        <td>域名</td> 
        <td>同步状态</td> 
        <td>子域名数量</td> 
        <td>最后更新时间</td> 
        <th></th> 
      </tr>
    </tfoot>
  </table>
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