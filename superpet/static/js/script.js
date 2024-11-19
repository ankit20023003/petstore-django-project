function updatequantity(operation,productId)
{

    const inputbox=document.getElementById("quantity"+productId);
    inputbox.value=parseInt(inputbox.value)+operation;
    


}