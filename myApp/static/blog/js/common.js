/**
 * Created by zhaohui on 18-2-17.
 */
$(function () {

    // var header_top  = document.getElementById('header_top')
    // header_top.onScroll = function () {
    //
    //     alert('sssssssss')
    //
    // }
    //
    //
    // var


    // $('#header_top').scroll(function () {
    //     alert('sssssssss')
    //     // scrollTop =document.documentElement.scrollTop || document.body.scrollTop
    //     // if (scrollTop>100){
    //     // }
    //
    // })


    var main_height = $('main').offset().top;
    $(window).scroll(function () {

        var this_scrollTop =$(this).scrollTop();
        if (this_scrollTop>main_height-50){




            $('.header_top').css({
                backgroundColor:"rgb(255,255,255,1)"
            }

            )


        }else{

            $('.header_top').css(
                {backgroundColor:"rgb(255,255,255,0)"}

                )
        }

    })



})