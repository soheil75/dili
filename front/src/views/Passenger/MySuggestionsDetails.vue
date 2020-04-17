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
                    <p class="font-12 px-4">{{ware.Description}}</p>
                    <div class="divider"></div>
                    <a class="btn w-50 info-button link-button" :href="ware.Url">مشاهده کالا</a>
                    <div class="pass-info">
                        <h4 class="title">تاریخ پیشنهادی شما : <span>2 خرداد 1399</span></h4>
                        <div class="divider"></div>
                        <h4 class="title">مبلغ پیشنهادی شما : <span>150دلار</span></h4>
                        <div class="divider"></div>
                        <h4 class="title">پیام شما</h4>
                        <p class="font-12 px-4">کالای شما را در اسرع وقت به دست شما می رسونم</p>
                        <div class="divider"></div>
                    </div>
                    <div class="MyContent">
                        <button @click="processToggle" class="toggle-btn link-button">وضعیت سفارش<i :class="{'rotate':rotate2}" class='fas fa-angle-down angel'></i></button>
                        <vue-slide-up-down :active="process" :duration="400">
                            <div class="stage" v-for="(stage, index) in ware.stages" :key="index">
                                <div :class="{stageActive:stage.active}"><i class='fas fa-caret-left'></i>
                                    <h4 class="title">{{stage.level}}</h4>
                                </div>
                            </div>
                        </vue-slide-up-down>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import Header from '@/components/Header.vue'
import VueSlideUpDown from 'vue-slide-up-down'
export default {
    components: {
        VueSlideUpDown,
        Header
    },
    data: () => ({
        ware: '',
        title: 'پیشنهاد خرید',
        backlink: '/MySuggestionsPass',
        comments: false,
        process: false,
        rotate: false,
        rotate2: false
    }),
    methods: {
        getware() {
            const path = `/api/myorderdetails/${this.$route.params.id}`;
            axios.get(path)
                .then((res) => {
                    this.ware = res.data.ware;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        commentsToggle() {
            this.comments = !this.comments;
            this.rotate = !this.rotate;
        },
        processToggle() {
            this.process = !this.process;
            this.rotate2 = !this.rotate2;
        },
    },
    created() {
        this.getware();
    },
}
</script>

<style lang="css">
.pass-info {
    background: #e9ecef;
    padding-top: 20px;
    margin-top: 20px;
    border-radius: 4px;
}

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

.stageActive {
    color: #626261;
}

.stageActive i {
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

.toggle-btn {
    display: block;
    margin: 10px auto;
    border: none;
    background: #f1f1f1;
    width: 100%;
    padding: 10px 0;
    border-left: 0;
    border-radius: 4px;
    border-right: 0;
    position: relative;
    box-shadow: none;
    font-weight: 600;
}

.angel {
    position: absolute;
    left: 20px;
    top: 13px;
}

.rotate {
    transform: rotate(180deg);
    transition: 0.4s ease all;
}
</style>
