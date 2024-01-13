// this function will verify wheter the next case whre we want to is empty and exist 
function exist_and_empty(i,j,n,square) {
    if( 0<=i && 0<=j && i<=n-1 && j<=n-1){
        if(square[i][j] == 0){
            return 0;
        }
        else{
            return 1 ;
        }
    }
    else {
        return 1 ;
    }
}


function magic_square() {
    let n = parseInt(document.getElementById("size").value);
    // down there we try to see wether the square size is pair or not, if it is pair we add 1 to this size because we cannot generate a magic-square with a pair size
    if (n%2 ===0) {
        n += 1;
    }


    // square creat
    var square = new Array(n);
    for (var i = 0; i < square.length; i++) {
      square[i] = new Array(n);
    }
    // matrix filling
    for (let i = 0; i < square.length; i++) {
        for (let j = 0; j < square.length; j++) {
            square[i][j] = 0;
        }        
    }

    let index_i = 0;
    let index_j = Math.floor(n/2);
    let k = 1;
    let insert_nomber = k;
    square[index_i][index_j] = insert_nomber;
    insert_nomber +=1


    for ( k = 2; k <= n*n; k++) {

        if (exist_and_empty(index_i-1,index_j+1,n,square)==0) {
            index_i -= 1;
            index_j += 1; 
            square[index_i][index_j] = insert_nomber;
            insert_nomber+=1;
        }
        else if (exist_and_empty(index_i-1,(index_j-(n-1)),n,square)==0) {
            index_i -= 1;
            index_j =(index_j-(n-1));
            square[index_i][index_j] = insert_nomber;
            insert_nomber+=1;
        }
        else if (exist_and_empty((index_i+(n-1)),index_j+1,n,square)==0) {
            index_i = n-1;
            index_j +=1 ;
            square[index_i][index_j] = insert_nomber;
            insert_nomber+=1;
        }
        else{
            console.log("error")
            index_i +=1 ;
            index_j = index_j;
            square[index_i][index_j] = insert_nomber;
            insert_nomber+=1;
        }
        console.log(square);
    }


    // Création d'un tableau HTML
    var tableau = document.createElement("table");
    // Appliquer des styles au tableau
    tableau.style.borderCollapse = "collapse";
    tableau.style.border = "1px solid #ccc";
    tableau.style.marginTop = "90px";


    // Création des lignes du tableau
    for (var i = 0; i < n; i++) {
    var ligne = document.createElement("tr");

    // Création des cellules de la ligne
    for (var j = 0; j < n; j++) {   
        var cellule = document.createElement("td");
        // var texte = document.createTextNode("Ligne " + i + ", Cellule " + j);
        var texte = document.createTextNode(square[i][j]+ "        ");
        cellule.appendChild(texte);
        cellule.style.padding = "10px";
        cellule.style.backgroundColor = "white";
        cellule.style.border = "1px solid #ccc";
        ligne.appendChild(cellule);
    }

    // Ajout de la ligne au tableau
    tableau.appendChild(ligne);
    }

    // Ajout du tableau à un élément existant dans la page (par exemple, un élément avec l'id "conteneur")
    var conteneur = document.getElementById("magic-square");
    conteneur.appendChild(tableau);
}