function printHello( num ){
    if( num === 0 ){
        return "";
    }
    return "Hello\n" + printHello( num - 1 );
}

console.log( printHello( 10 ) );