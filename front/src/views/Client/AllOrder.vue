<template>
<div>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6 m-md-auto">
                <HeaderSlide :title="title"></HeaderSlide>
                <div class="wares">
                    <router-link :to="'/OrderDetails/'+ ware.id " v-for="(ware, index) in wares" :key="index">
                        <div class="ware">
                            <div class="img-box">
                                <img :src="require(`@/assets/${ware.imagePath}`)" :alt="ware.Title">
                            </div>
                            <div class="text-box">
                                <h4>نام کالا : <span>{{ ware.Title }}</span></h4>
                                <h4>کشور مبدا : <span>{{ ware.Origin }}</span></h4>
                            </div>
                        </div>
                    </router-link>
                </div>
                <router-link class="add-btn" to="/NewOrder"><i class='fas fa-plus'></i></router-link>
            </div>
        </div>
    </div>
    <Footer></Footer>
</div>
</template>

<script>
import axios from 'axios';
import Footer from '@/components/Footer';
import HeaderSlide from '@/components/HeaderSlide.vue';

export default {
    components: {
        Footer,
        HeaderSlide
    },
    data: () => ({
        title: 'همه سفارشات',
        wares:'',
    }),
    methods: {
        getwares() {
            const path = 'http://localhost:5000/allorder';
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
.img-box {
    min-width: 100px;
}

.wares {
    position: relative;
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
    max-height: 100px;
    display: block;
    margin: auto;
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
