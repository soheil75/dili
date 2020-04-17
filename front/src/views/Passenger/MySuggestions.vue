<template>
<div>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6 m-md-auto">
                <HeaderSlide :title="title"></HeaderSlide>
                <div class="wares mt-3">
                    <router-link :to="'/MySuggestionsDetailsPass/'+ ware.id " v-for="(ware, index) in wares" :key="index">
                        <div class="ware">
                            <div class="img-box">
                                <img :src="require(`@/assets/${ware.imagePath}`)" :alt="ware.Title">
                            </div>
                            <div class="text-box">
                                <h4>نام کالا : <span>{{ ware.Title }}</span></h4>
                                <h4>کشور مبدا : <span>{{ ware.Origin }}</span></h4>
                                <h4 class="limit-chars">کد سفارش : <span>{{ware.id}}-DDS</span></h4>
                                <h4>تاریخ تحویل : <span>{{ ware.Date }}</span></h4>
                            </div>
                        </div>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
    <Footer></Footer>
</div>
</template>

<script>
import axios from 'axios';
import Footer from '@/components/PassFooter'
import HeaderSlide from '@/components/HeaderSlide.vue'

export default {
    components: {
        Footer,
        HeaderSlide
    },
    data: () => ({
        title: 'پیشنهادات من',
        wares: '',
    }),
    methods: {
        getwares() {
            const path = '/api/myorder';
            axios.get(path)
                .then((res) => {
                    this.wares = res.data.wares;
                })
                .catch((error) => {
                    console.error(error);
                });
        }
    },
    created() {
        this.getwares();
    }
}
</script>

<style>
.form-control {
    background-color: #f3f3f3;
}

.wares {
    position: relative;
}

.wares:last-child {
    margin-bottom: 72px;
}

.ware {
    display: flex;
    justify-content: right;
    align-items: center;
    text-align: right;
    padding: 10px 5px;
    margin-bottom: 5px;
    box-shadow: 0 3px 9px #e4e4e4;
}

.ware img {
    max-width: 100px;
    border-radius: 4px;
}

.text-box {
    padding: 0 10px;
}

.text-box h4 {
    font-size: 13px;
    font-weight: 600;
    line-height: 1.4;
}

.text-box span {
    font-weight: 400;
}

.add-btn {
    position: fixed;
    bottom: 65px;
    left: 20px;
    background: #b8221f;
    background: linear-gradient(to left, #b8221f, #e64135);
    color: #fff;
    padding: 15px 20px;
    border-radius: 50%;
    border: none;
    box-shadow: 0 3px 6px #b79e9d;
}

.add-btn i {
    vertical-align: sub;
}
</style>
