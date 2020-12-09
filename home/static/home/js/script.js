console.log("Its working")


function conf_sub() {
    var form = document.getElementById('cmform');
    var name = document.forms['cmform']['name'].value
    var email = document.forms['cmform']['email'].value
    var body = document.forms['cmform']['body'].value
    console.log(name.trim());
    console.log(email.trim());
    console.log(body.trim())
    if (name.trim() != '' && email.trim() != '' && body.trim() != '') {
        console.log("I am in")
        function sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }
        async function demo() {
            console.log('Taking a break...');
            var confirm = () => swal("Comment Added!", "You comment has been posted!", "success");
            confirm()
            await sleep(2000);
            form.submit();
            
        }
        demo()
        
    }
}


var form = document.getElementById('sub');

function deletec(word) {
    swal({
        title: "Are you sure?",
        text: "Once deleted, you will not be able to recover this imaginary file!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
        .then((willDelete) => {
            if (willDelete) {
                form.setAttribute('onsubmit', 'return true');
                swal(word+" has been deleted! Redirecting......", {
                    icon: "success",
                });
                function sleep(ms) {
                    return new Promise(resolve => setTimeout(resolve, ms));
                }
                async function demo() {
                    console.log('Taking a break...');
                    var confirm = () => swal("Comment Deleted!", "Your " +word+" has been deleted!", "success");
                    confirm()
                    await sleep(2000);
                    form.submit();
                    
                }
                demo()
            } else {
                swal(word+" not deleted!");
            }
        });
}

// if( document.myForm.Name.value == "" ) {
//     alert( "Please provide your name!" );
//     document.myForm.Name.focus() ;
//     return false;
//  }
//  if( document.myForm.EMail.value == "" ) {
//     alert( "Please provide your Email!" );
//     document.myForm.EMail.focus() ;
//     return false;
//  }