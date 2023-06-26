import axios from "axios"

// TODO: set hostname + port dynamically

export function getWagtailPage(id) {
  return axios.get(`//localhost:8000/api/v2/pages/${id}/`)
}

export function getWagtailPageByPath(path) {
  return axios.get(`//localhost:8000/api/v2/pages/find/?html_path=${path}`)
}

export function getWagtailPagesInMenu() {
  return axios.get(
    "//localhost:8000/api/v2/pages/?show_in_menus=true&fields=_,html_url,title"
  )
}

export function getWagtailImage(id) {
  return axios.get(`//localhost:8000/api/v2/images/${id}/`)
}

export function getWagtailDocument(id) {
  return axios.get(`//localhost:8000/api/v2/documents/${id}/`)
}
