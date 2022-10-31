const dialog = document.createElement("dialog");

// Type signature of onclose:
// onclose: ((this: GlobalEventHandlers, ev: Event) => any) | null;
dialog.onclose = function () {}; // Compiles despite function signature mismatch

dialog.onclose = window.close;   // Which can lead to bugs like these
