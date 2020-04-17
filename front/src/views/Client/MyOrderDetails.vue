<template>
<div>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6 m-md-auto">
                <header class="header">
                    <router-link class="back-btn" to="/MyOrder">
                        <i class="far fa-angle-left ver-middle"></i>
                    </router-link>
                    <h1>جزییات سفارش</h1>
                    <button class="modal-toggle" v-b-modal.delete-modal><i class="far fa-ellipsis-v"></i></button>
                </header>
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
                    <div class="MyContent">
                        <button @click="commentsToggle" v-if="ware.comments.length > 0" class="toggle-btn link-button">پیشنهادات مسافران
                            <span>({{ware.comments.length}})</span><i :class="{'rotate':rotate}" class='fas fa-angle-down angel'></i>
                        </button>
                        <vue-slide-up-down :active="comments" :duration="400" v-if="ware.comments.length > 0">
                            <ul>
                                <li v-for="(comment, index) in ware.comments" :key="index">
                                    <div class="comment-par">
                                        <div class="comment-par-top">
                                            <h4 class="title">{{comment.name}}</h4>
                                            <div class="star">
                                                <span class="fa fa-star checked" v-for="(ware, index) in comment.rate" :key="index"></span>
                                            </div>
                                        </div>
                                        <h4 class="title font-13">تاریخ تحویل کالا : <span>{{comment.date}}</span></h4>
                                        <h4 class="title font-13">پاداش پیشنهادی : <span>{{comment.cost}}</span> دلار </h4>
                                        <p class="font-13 m-0">{{comment.text}}</p>
                                    </div>
                                </li>
                            </ul>
                        </vue-slide-up-down>
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
                <div>
                    <b-modal ref="DeleteModal" id="delete-modal" header-bg-variant="warning" header-text-variant="dark" hide-footer>
                        <template v-slot:modal-header="{ close }">
                            <h5 class="w-100 m-0 text-center">تنظیمات</h5>
                            <!-- Emulate built in modal header close button action -->
                            <b-button class="d-none" size="sm" variant="light" @click="close()">بستن</b-button>
                        </template>
                        <h4 class="h6 text-center">آیا مایل به حذف سفارش خود هستید ؟ </h4>
                        <b-form class="w-100 text-center" @submit="onSubmit">
                            <b-button class="btn py-1 px-4 mr-1 btn-light" @click="hideModal" variant="primary">خیر</b-button>
                            <b-button class="btn py-1 px-4 mr-3 btn-danger" type="submit" variant="primary">بله</b-button>
                        </b-form>
                    </b-modal>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import VueSlideUpDown from 'vue-slide-up-down'
export default {
    components: {
        VueSlideUpDown
    },
    data: () => ({
        ware: '',
        comments: false,
        process: false,
        rotate: false,
        rotate2: false
    }),
    methods: {
        getware() {
            const path = `http://localhost:5000/myorderdetails/${this.$route.params.id}`;
            axios.get(path)
                .then((res) => {
                    this.ware = res.data.ware;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        delete(payload) {
            const path = `http://localhost:5000/myorderdetails/${this.ware.id}`;
            axios.delete(path, payload)
                .then(() => {
                    this.$router.push('/MyOrder');
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.log(error);
                });
        },
        onSubmit(evt) {
            evt.preventDefault();
            this.$refs.DeleteModal.hide();
            const payload = {
                id: this.ware.id,
            };
            this.delete(payload);
            this.initForm();
        },
        hideModal() {
            this.$refs['DeleteModal'].hide()
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
.modal-backdrop {
    background-color: #0006 !important;
}

.modal-dialog {
    margin-top: 30%;
}

.modal-content {
    border: none;
    border-radius: 4px;
}

.back-btn {
    font-size: 18px;
    color: #fff;
    padding: 10px;
    position: absolute;
    left: 20px;
    top: 13px;
}

.header {
    text-align: center;
    padding: 20px;
    background: #b8221f;
    background: linear-gradient(to left, #b8221f, #e64135);
    color: #fff;
    margin: 0 -15px;
    position: relative;
}

.header h1 {
    font-size: 18px;
    font-weight: 600;
    margin: 0;
    padding-top: 5px;
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
