<template>
<div>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6 m-md-auto">
                <Header :title="title" :link="backlink"></Header>
                <div class="info">
                    <img :src="require(`@/assets/${ware.imagePath}`)" :alt="ware.Title">
                    <h4 class="ware-name">{{ware.Title}}</h4>
                    <div class="divider"></div>
                    <h4 class="route font-14 pt-0"><i class="fal fa-flip-horizontal p-2 fa-plane-departure"></i>مبدا : <span>{{ware.Origin}}</span></h4>
                    <h4 class="route font-14 pt-0"><i class="fal fa-flip-horizontal p-2 fa-plane-arrival"></i>مقصد : <span>{{ware.Destination}}</span></h4>
                    <div class="divider"></div>
                    <h4 class="title">تاریخ تحویل کالا : <span>{{ware.Date}}</span></h4>
                    <h4 class="title font-13 red-color" v-if="!ware.Accept"><i class="fal fa-exclamation-triangle pl-2"></i>عدم دریافت کالا بعد از تاریخ فوق</h4>
                    <div class="divider"></div>
                    <h4 class="title">توضیحات کالا</h4>
                    <p class="font-12 px-4 m-0">{{ware.Description}}</p>
                    <div class="divider"></div>
                    <a class="btn w-50 info-button link-button" :href="ware.Url">مشاهده کالا</a>
                    <router-link class="btn submit-btn" :to="'/AcceptOrderPass/'+ ware.id ">پیشنهاد خرید</router-link>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import Header from '@/components/Header.vue'

export default {
    components: {
        Header,
    },
    data() {
        return {
            title: 'جزییات درخواست',
            backlink: '/AllOrderPass',
            ware: '',
        }
    },
    methods: {
        getware() {
            const path = `http://localhost:5000/api/acceptOrder/${this.$route.params.id}`;
            axios.get(path)
                .then((res) => {
                    this.ware = res.data.ware;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
    },
    created() {
        this.getware();
    }
}
</script>

<style lang="css">
.stage {
    color: #b1b1b1;
}

.stage h4 {
    display: inline-block;
}

.stage i {
    width: 15px;
    text-align: center;
    vertical-align: middle;
}

.stage-active {
    color: #626261;
}

.stage-active i {
    color: #b8221f;
}

.comment-par {
    text-align: right;
    background: #f1f1f1;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 5px;
}

.comment-par-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>
