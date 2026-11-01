/* components return jsx elements which look like html with ability to use JS expressions to insert data dynamically
any html tag can be used in jsx
some html attributes have different names in jsx, the rest are the same
jsx elements can contain other components inside them
*/

import "./style.css"; // css import, will add the styles in the file to the root of the web page with no scoping
import otherComponent from "./otherComponent"; // compoenent import, imports the default export component from the jsx file which can be used as a subcomponent in other components

function Component() { // function component, must start with capital letter
    const variable = "Hello, World!"; // any valid JS code can be used here
    const link = "https://www.example.com"; 
    return ( // must return one top level JSX element 
        <div // regular HTML element tags can be used
            className="component" // 'className' refers to 'class' in HTML

            href={link} // attribute with dynamic value
        > variable = {variable} </div> 
        // any valid JS expressions inside {} will be evaluated and the returned value will be inserted as text inplace of the {}
        // the result value of the expression can be any valid JS type except for booleans and objects, objects are valid in some attributes like 'style' 
        // to use inline objects as value in {}, use double curly braces {{}} 
        // values of an array will be concatenated together directly as a single text
        // dynamic values can be used in any attribute and in the content of elements, but not in the tag name or attribute names

        
        
        // any valid JS expressions inside {} will be evaluated and the returned value will be converted to strings and inserted in their place, booleans and objects aren't valid
    )

}


function AnotherComponent() { 
    return (
        <div>
            <Component /> // self closing component tag, used when the component doesn't have any children
            <Component> // opening tag of a component with children
                <p>This is a child element</p> // child element of the component, can be any valid JSX template with any number of children
            </Component> // closing tag of a component with children
        </div>
    )
}
export default AnotherComponent; // exporting the component as default to be imported in other files  