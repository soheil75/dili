<template>
<div>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6 m-md-auto">
                <header class="header">
                    <h1>حساب کاربری</h1>
                </header>
                <div class="top">
                    <img src="../assets/man.png" alt="">
                    <p>علی احمدی پور</p>
                </div>
                <div class="middle">
                    <div class="middle-right">
                        <div class="star">
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star"></span>
                            <span class="fa fa-star"></span>
                        </div>
                        <p>امتیاز :<span class="pr-1">5</span></p>
                    </div>
                    <div class="middle-left">
                        <img src="../assets/basket.png" alt="">
                        <p>سفارش :<span class="pr-1">20</span></p>
                    </div>
                </div>
                <div class="bottom">
                    <button class="btn button"><i class='fas icon fa-phone pl-2'></i>تماس با پشتیبانی</button>
                </div>
                <div class="bottomm">
                    <button class="btn button"><i class='fas icon fa-sign-out-alt pl-2'></i>خروج از حساب کاربری</button>
                </div>
            </div>
        </div>
    </div>
    <Footer></Footer>
</div>
</template>

<script>
import Footer from '../components/Footer'

export default {
    components: {
        Footer
    }
}
</script>

<style>
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

.top {
    padding: 15px;
    text-align: center;
    border-bottom: 1px solid #cacaca;
    padding-bottom: 0px;
}

.top img {
    max-width: 120px;
    display: block;
    margin: auto;
}

.top p {
    margin: 10px 0;
}

.middle {
    display: flex;
    align-items: flex-end;
    justify-content: space-evenly;
    border-bottom: 1px solid #cacaca;
}

.star {
    padding-bottom: 5px;
}

.fa-star {
    color: #ebb800;
}

.middle p {
    margin: 10px 0;
    font-weight: 600;
}

.middle-right {
    padding: 20px;
    text-align: center;
}

.middle-left {
    padding: 20px;
    text-align: center;
}

.middle-left img {
    max-width: 50px;
    display: block;
    margin: auto;
}

.bottom {
    text-align: center;
    padding: 20px;
    border-bottom: 1px solid #cacaca;
}

.bottomm {
    text-align: center;
    padding: 20px;
}

.button {
    padding: 10px;
    background-color: #f1f1f1;
    font-size: 16px;
    color: #626261;
}

.icon {
    vertical-align: middle;
    font-size: 20px;
}
</style>
