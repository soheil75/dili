<template>
<div class="container">
    <div class="row">
        <div class="col-12 col-md-6 m-md-auto">
            <Header :title="title" :link="backlink"></Header>
            <div class="info">
                <img :src="require(`@/assets/${ware.imagePath}`)" :alt="ware.Title">
                <h4 class="ware-name">{{ware.Title}}</h4>
                <div class="divider"></div>
                <h4 class="route"><i class="fal fa-flip-horizontal p-2 fa-plane-departure"></i>مبدا : <span>{{ware.Origin}}</span></h4>
                <h4 class="route"><i class="fal fa-flip-horizontal p-2 fa-plane-arrival"></i>مقصد : <span>{{ware.Destination}}</span></h4>
                <div class="divider"></div>
                <a class="btn w-50 info-button link-button" :href="ware.Url">مشاهده کالا</a>
                <button @click="onSubmit" class="btn mt-3 w-50 info-button submit-btn">افزودن به سفارشات من</button>
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
        Header
    },
    data() {
        return {
            title: 'جزییات سفارش',
            backlink: '/AllOrder',
            ware: '',
        }
    },
    methods: {
        getware() {
            const path = `http://localhost:5000/orderdetails/${this.$route.params.id}`;
            axios.get(path)
                .then((res) => {
                    this.ware = res.data.ware;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        addToMyOrder(payload) {
            const path = `http://localhost:5000/orderdetails/${this.ware.id}`;
            axios.post(path, payload)
                .then(() => {
                    this.$router.push('/MyOrder');
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.log(error);
                    this.getware();
                });
        },
        onSubmit(evt) {
            evt.preventDefault();
            const payload = {
                id: this.ware.id,
            };
            this.addToMyOrder(payload);
        },
    },
    created() {
        this.getware();
    }
}
</script>

<style>
.button-bot {
    background: #b8221f;
    background: linear-gradient(to left, #b8221f, #e64135);
    color: #fff;
    box-shadow: 0 5px 10px #e8a39e;
}

.info img {
    max-width: 150px;
    display: block;
    margin: 5px auto 30px;
}

.info {
    padding: 20px 0;
    text-align: center;
}

.ware-name {
    font-size: 18px;
    font-weight: bold;
}
</style>
