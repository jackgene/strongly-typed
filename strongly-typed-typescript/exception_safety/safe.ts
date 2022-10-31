// function safeDecodeURI(encodedURI: string): string | Error {
//   try {
//     return decodeURI(encodedURI);
//   } catch (e: any) {
//     return e instanceof Error ? e : Error(e);
//   }
// }
//
// const urlOrErr: string | Error = safeDecodeURI("bad%c3url");
// if (!(urlOrErr instanceof Error)) console.log(urlOrErr.toLowerCase());
