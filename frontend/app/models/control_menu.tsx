import { useState, useEffect } from "react";


export function Menu() {
    return (
        <div>
            <ViewSpecimen/>
            <CreateNewSpecimen/>
        </div>
    )
}

interface specimen_data {
    id: number;
    collectioneventid: number;
    specimenno: string;
    taxorder: string;
    taxsuborder: string;
    taxsuperfamily: string;
    taxfamily: string;
    taxsubfamily: string;
    taxtribe: string;
    taxsubtribe: string;
    taxgenus: string;
    taxsubgenus: string;
    taxspecies: string;
    taxsubspecies: string;
    authority: string;
    authorityyear: string;
    identifier: string;
    iddate: string;
    verifier: string;
    verifierdate: string;
    idnote: string;
    specimennote: string;
}

const create_fields = [
  "collectioneventid", 
  "specimenno", 
  "taxorder", 
  "taxsuborder", 
  "taxsuperfamily", 
  "taxfamily", 
  "taxsubfamily", 
  "taxtribe", 
  "taxsubtribe", 
  "taxgenus", 
  "taxsubgenus", 
  "taxspecies", 
  "taxsubspecies", 
  "authority", 
  "authorityyear", 
  "identifier", 
  "iddate", 
  "verifier", 
  "verifierdate", 
  "idnote", 
  "specimennote", 
]

const disp_fields = [
  "id", 
  ...create_fields
]
  


function ViewSpecimen() {
    const [data, setData] = useState<specimen_data[]>([]);
    useEffect(() => {
      fetch("http://localhost:8000/specimens/all").then((response) => {
        if(response.ok) {
          response.json().then((json) => {
            setData(json);
          });
        }
      });
    }, []);

    return (
        <div>
          <h1>View Specimen</h1>
          <table>
          <tbody>
            <tr>
              {disp_fields.map((field, i) => (
                <th key={i}> {field} </th>
              ))}
            </tr>
            {data.map((specimen, i) => (
              <tr key={i}> 
                {disp_fields.map((field, j) => (
                  // TODO: figure out a better way of doing this which typescript likes
                  <td key={j}> {specimen[field]} </td>
                ))}
              </tr>
            ))}
          </tbody>
          </table>
        </div>
    )
}


function CreateNewSpecimen() {
  return (
      <div>
        <h1>Create New Specimen</h1>

        <form action="http://localhost:8000/specimens/create" method="post">
          {create_fields.map((field, i) => (
            <div key={i}>
              <label htmlFor={field}>{field}</label>
              <input type="text" id={field} name={field} />
            </div>
          ))}

          <br/><input type="submit" value="Create" />
        </form>
      </div>
  )
}
