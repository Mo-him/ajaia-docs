const API = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';
export function token(){ return localStorage.getItem('ajaia_token') || ''; }
async function request(path:string, options:RequestInit={}){
  const headers = new Headers(options.headers || {}); if(!headers.has('Content-Type') && options.body) headers.set('Content-Type','application/json'); if(token()) headers.set('Authorization',`Bearer ${token()}`);
  const res=await fetch(`${API}${path}`,{...options,headers}); const data=await res.json().catch(()=>({})); if(!res.ok) throw new Error(data.detail || 'Request failed'); return data;
}
export const api={
 login:(email:string,password:string)=>request('/auth/login',{method:'POST',body:JSON.stringify({email,password})}),
 me:()=>request('/auth/me'),
 documents:()=>request('/documents'),
 getDocument:(id:number)=>request(`/documents/${id}`),
 create:(title:string)=>request('/documents',{method:'POST',body:JSON.stringify({title,content:'<p>Start writing your document...</p>'})}),
 update:(id:number,title:string,content:string)=>request(`/documents/${id}`,{method:'PUT',body:JSON.stringify({title,content})}),
 remove:(id:number)=>request(`/documents/${id}`,{method:'DELETE'}),
 share:(id:number,email:string)=>request(`/documents/${id}/share`,{method:'POST',body:JSON.stringify({email})}),
 shares:(id:number)=>request(`/documents/${id}/shares`),
 importFile:async(file:File)=>{ const form=new FormData(); form.append('file',file); const res=await fetch(`${API}/documents/import`,{method:'POST',headers:{Authorization:`Bearer ${token()}`},body:form}); const d=await res.json(); if(!res.ok) throw new Error(d.detail||'Import failed'); return d; }
};
