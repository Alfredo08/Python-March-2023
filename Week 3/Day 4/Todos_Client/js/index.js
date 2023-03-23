
async function loadTodos( element ){
    let url = "http://127.0.0.1:5001/api/todos";
    let response = await fetch( url );
    console.log( response );
    let data = await response.json();
    console.log( data );

    let results_Div = document.querySelector( ".results" );
    results_Div.innerHTML = "";
    for( let i = 0; i < data.length; i ++ ){
        results_Div.innerHTML += 
        `<p>
            ${data[i].name} - ${data[i].status}
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