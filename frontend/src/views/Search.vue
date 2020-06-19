<style scoped>
    .search {
        padding-top: 24px;
        overflow: hidden;
        zoom: 1;
    }

    .left {
        float: left;
        margin: 0 20px;
        text-align: center;
    }

    .right {
        width: 600px;
        overflow: hidden;
        zoom: 1;
    }

    img {
        padding-top: 4px;
        text-align: center;
    }
</style>

<template>
    <div class="search">
        <div class="left">
            <img src="./../assets/wikinp.png" @click="goHome">
        </div>
        <div class="right">
            <a-input-search
                    v-focus v-model="searchText"
                    size="large"
                    @search="searchResult"/>
        <div> search time: </div>
            <div v-for="item in result" v-bind:key="item.id">
                <searchResult :info="item"></searchResult>
            </div>
        </div>
        <div class="left">
            <img src="./../assets/about.png" @click="goAbout">
        </div>


    </div>
</template>

<script>
    import axios from 'axios'
    import SearchResult from "../components/SearchResult";

    export default {
        name: "Search",
        data() {
            return {
                searchText: "",
                result: [],
            }
        },
        components: {
            searchResult: SearchResult
        },

        methods: {
            goHome() {
                this.$router.push("/")

            },
            goAbout() {
                this.$router.push("/about")

            },
            searchResult() {
                if (this.searchText !== '') {
                    this.$router.push({path: `/search`, query: {q: this.searchText}})
                }
                console.info("router query:" + this.$route.query.q)
                console.info("search text: " + this.searchText)


                const path = location.href.replace(this.$route.path,'').replace(this.$route.query.q, '') .replace('?q=', '')+ "/api/search?q=" + this.$route.query.q;
                axios.get(path)
                    .then((res) => {
                        this.result = res.data;
                        console.info(res)
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            }
        },

        created() {
            this.searchResult()
        },

        watch: {
            '$route'(to, from) {
                // 对路由变化作出响应...
                this.searchResult()
            }
        }
    }
</script>

