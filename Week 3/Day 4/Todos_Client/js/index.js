
async function loadTodos( element ){
    let url = "http://127.0.0.1:5001/api/todos";

    let settings = {
        method : "GET"
    };

    let response = await fetch( url, settings );
    let data = await response.json();

    let results_Div = document.querySelector( ".results" );
    results_Div.innerHTML = "";
    for( let i = 0; i < data.length; i ++ ){
        results_Div.innerHTML += 
        `<p id="todo_${data[i].id}">
            ${data[i].name} - ${data[i].status} 
            <button onclick="deleteTodo(${data[i].id})">
                Delete
            </button>
         </p>
        `;
    }
    /*
    let url = "https://pokeapi.co/api/v2/pokemon/";

    let response = await fetch( url );
    console.log( response );
    let data = await response.json();
    console.log( data );

    let results_Div = document.querySelector( ".results" );
    results_Div.innerHTML = "";
    for( let i = 0; i < data.results.length; i ++ ){
        results_Div.innerHTML += 
        `<p>
            ${data.results[i].name}
        </p>
        `;
    }
    */

}

async function deleteTodo( todoId ){
    let url = `http://127.0.0.1:5001/api/delete/todo/${todoId}`;
    let settings = {
        method : "DELETE"
    };

    let response = await fetch( url, settings );
    console.log( response );

    document.querySelector( `#todo_${todoId}` ).remove();
}

async function addTodo( event ){
    event.preventDefault();
    let url = "http://127.0.0.1:5001/api/new/todo";
    
    let data = {
        name : document.querySelector( '#todo_name' ).value,
        status : document.querySelector( '#todo_status' ).value,
        user_id : 6
    };

    let settings = {
        method : "POST",
        headers : {
            "Content-type" : "application/json"
        },
        body : JSON.stringify( data )
    }

    let response = await fetch( url, settings );
    let responseData = await response.json();
    console.log( responseData );

}