<template>
  <div>
    <a-card hoverable>
        <a-card-meta
        :title="info._source.bookname+' ('+info._source.year+')'"
        :description="info._source.author+' / '+info._source.category+' / '+info._source.awards + ' / '+ info._source.IMDB">
        <a-avatar style="backgroundColor:#d04713" slot="avatar">{{info._source.zh_author}}</a-avatar>
        </a-card-meta>
      <div class="describe">“{{info._source.commentary}}”</div>
      <div style="text-align: right">{{info._score}}</div>
       <img :src="info._source.cover">
    </a-card>
  </div>
</template>

<script>
export default {
  name: "SearchResult",
  props: ["info"]
};
</script>

<style scoped>
div {
  margin-top: 12px;
}

.describe {
  padding: 12px 0 0 0;
  text-align: center;
  color: #d04713;
}
</style>