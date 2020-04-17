<template>
    <div class="footer">
        <router-link to="/MyOrder">
            <div class="box">
                <i class='fas fa-inbox icon-footer'></i>
                <h4>سفارشات من</h4>
            </div>
        </router-link>    
        <router-link to="/AllOrder">
            <div class="box">
                <i class='fas fa-list icon-footer'></i>
                <h4>همه سفارشات</h4>
            </div>
        </router-link>    
        <router-link to="/MyAccount">
            <div class="box">
                <i class='fas fa-user icon-footer'></i>
                <h4>حساب کاربری</h4>
            </div>
        </router-link>
    </div>
</template>

<style>
    .footer{
        background: #f3f3f3;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: space-around;
        z-index: 999;
        padding: 8px 0;
    }
    .box{
        padding: 8px 12px;
        color: #8f8f8e;
        text-align: center;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .box h4{
        font-size: 13px;
        margin: 5px 8px;
        font-weight: 400;
        display: none;
    }
    .icon-footer{
        vertical-align: middle;
        font-size: 18px;
        width: 20px;
        text-align: center;
    }
    .footer a{
        color: #8f8f8e;
    }
    a.router-link-exact-active .box{
        color: #ffffff;
        font-weight: 600;
        background: #b8221f;
        border-radius: 25px;
        background: -webkit-linear-gradient(to left, #b8221f, #e64135);  /* Chrome 10-25, Safari 5.1-6 */
        background: linear-gradient(to left, #b8221f, #e64135); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        box-shadow: 0px 3px 6px #b59d9c;

    }
    a.router-link-exact-active .box .icon-footer{
        font-size: 16px;
    }
    a.router-link-exact-active .box h4{
        color: #fff;
        font-weight: 600;
        display: block;
    }
    a:hover,a:visited,a:focus{
        text-decoration: none !important;
    }
</style>