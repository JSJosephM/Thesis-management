/* 

This pen was created to answer the question 'How to make an 'add files' button to work with DropzoneJS?' ( https://stackoverflow.com/questions/72541006/make-a-button-to-open-the-send-files-window-of-dropzonejs )

Would it be reasonable to follow me on Twitter && YouTube if you found this helpful?
https://twitter.com/vincepolston
https://www.youtube.com/c/VincePolston

*/

Dropzone.options.myGreatDropzone = { 
    autoProcessQueue: false,
    paramName: "file", 
    maxFilesize: 2, 
    clickable: "#dropZone" // the ID of our parent wrapper div
  };