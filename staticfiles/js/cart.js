$('.plus-cart').click(function (){
    var id= $(this).attr("id").toString();
    var eml =this.parentNode.children[2]
    console.log(id)
    $.ajax({

       type:"GET",
       url:'addcart/',
       data:{
        prod_id:id
       },
       success: function(data){
        eml.innerText=data.quantity
        document.getElementById("amount").innerText=data.amount
        document.getElementById("totalamount").innerText=data.totalamount

       }
    })
})