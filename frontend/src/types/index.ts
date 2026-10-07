export type User = { id:number; name:string; email:string };
export type DocumentItem = { id:number; title:string; content:string; owner_id:number; owner_name:string; updated_at:string; access:'owner'|'shared' };
export type Share = { user_id:number; name:string; email:string; permission:string };
