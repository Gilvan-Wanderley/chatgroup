const setRoomActive = (romd_id) => {
  QsAll(".list-rooms li").forEach((el) => el.classList.remove("active"));
  Qs(`#room-${romd_id}`).classList.add("active");
  Qs("#selected-room").value = romd_id;
};

const getMessages = async(romd_id) => {
  const response = await fetch(`/${romd_id}`);
  const html = await response.text();
  Qs(".messages").innerHTML = html;
  setRoomActive(romd_id);
  Qs(".send-message").hidden = false
}

const sendMessage = async(data) =>{
  const response = await fetch(`/${data.room_id}/send`, {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": data.csrfmiddlewaretoken,
    },
    body: JSON.stringify(data),
  });
  const html = await response.text();

  Qs(".unique-message-container").insertAdjacentHTML("beforeend", html);
  Qs(".send-message").reset();
}

const getLastRoom = () => {
  Qs(".list-rooms li").click();
};

Qs('.send-message').addEventListener('submit', (e) =>{
  e.preventDefault();
  const data = Object.fromEntries(new FormData(e.target).entries());
  console.log()
  if (data.message != '')
  {
    sendMessage(data)
  }  
})